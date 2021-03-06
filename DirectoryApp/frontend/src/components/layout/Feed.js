import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getBlogs, getPodcasts, getFeeds, getMore,getFilter } from '../../actions/feeds'
import { URLSearchParams } from 'url';


const divStyle = {
    width : '50%'
  };

  const feedTitle = {
    backgroundColor : '#5bd1d7',
    minHeight : "49px"
  };

const cardStyle = {
    minHeight: '10rem'
};
  
export class Feed extends Component {
    constructor(props){
        // this.props.isLoading = false;
        super(props)
        // Sets up our initial state
        this.state = {
            isLoadingBlog:null,
            isLoadingPodcast:null
        };
        // Binds our scroll event handler
    window.onscroll = () => {

        const {
          state: {
            isLoadingBlog,
            isLoadingPodcast
          },
        } = this;
        // console.log(isLoadingBlog);
        // console.log(this.props.blog_next);
        // console.log(isLoadingPodcast);
        // console.log(this.props.podcast_next)
        // Bails early if:
        // * there's an error
        // * it's already loading
        // * there's nothing left to load
        // if(isLoading == this.props.blog_next) return;
        if(isLoadingBlog == this.props.blog_next && isLoadingPodcast == this.props.podcast_next) return;
        if (this.props.blog_next == null && this.props.podcast_next == null) return;

        // console.log(this.props.next)
        // if(this.props.blog_next == null) return;

        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
            // you're at the bottom of the page
            // alert('scrolling');
            // console.log(this.props.blog_next)
            // console.log(this.props.podcast_next)
            // this.props.isLoading = true;
            // this.props.getMore(this.props.blog_next);
            
            this.setState({
                isLoadingBlog:this.props.blog_next,
                isLoadingPodcast:this.props.podcast_next
            }, () =>{
                const more = {
                    "isLoadingBlog":this.props.blog_next,
                    "isLoadingPodcast":this.props.podcast_next
                }
                
                this.props.getMore(more);
            });
            
        }
  
        // Checks that the page has scrolled to the bottom
        /*if (
          window.innerHeight + document.documentElement.scrollTop
          === document.documentElement.offsetHeight
        ) {
        //   this.props.getMore(this.props.next);
        // console.log(this.props.next)
            // alert('scrolling')
            this.setState({isLoading:this.props.blog_next}, () =>{
                this.props.getMore(this.props.blog_next);
            });
        }*/
      };
    } 

    static propTypes = {
        feeds: PropTypes.array.isRequired,
        // getBlogs:PropTypes.func.isRequired,
        // getPodcasts:PropTypes.func.isRequired,
        getFeeds:PropTypes.func.isRequired,
    }

    componentDidMount() {
        // this.props.getBlogs()
        // this.props.getPodcasts()
        // console.log(this.props.selected)
        var parsedUrl = new URL(window.location.href);
        //console.log(parsedUrl.searchParams.get("q"));
        //console.log(parsedUrl)
        var search = parsedUrl.searchParams.get("q");
        if(!!search){
            this.props.getFilter(search)
        }
        else {
            this.props.getFeeds();
        }

        // this.props.getFeeds();
        // var parsedUrl = new URL(window.location.href);
        // console.log(parsedUrl.searchParams.get("q"));
        // console.log(parsedUrl)
        
    }

    /*componentDidUpdate(){
        // console.log('updated!!')
        if(this.props.refresh_feed){
            this.setState({
                isLoadingBlog:null,
                isLoadingPodcast:null
            })
        }
    }*/

    openInNewTab = (e) => {
        e.persist();
        e.preventDefault();
        var win = window.open(e.target.href, '_blank');
        win.focus();
    }
    
  render() {
    return (
      <div>
        <ol className="breadcrumb" style={feedTitle}>
            <li className="breadcrumb-item active"><h4 className="text-dark">{!this.props.selected? "Recently Added": `About ${this.props.selected}`}</h4></li>
        </ol>
        <div className="d-flex align-content-start flex-wrap">
            {/* <div className="card-deck"> */}
                {this.props.feeds.map(feed => (
                    <div key={feed.id} className="col-md-6 col-xl-4 p-2">
                        <div className="card border-light rounded-lg shadow w-100 border-0" style={cardStyle}>
                            {/* { !!feed.author &&
                             <div className="card-header border-bottom-0 border-0" style={feedTitle}>{feed.author}</div>
                            } */}
                            
                             <div className="card-header border-bottom-0 border-0" style={feedTitle}>
                             { (feed.itemType === "BLOG") &&
                                <i className="fas fa-blog"></i>
                                }
                                { (feed.itemType === "PODCAST") &&
                                <i className="fas fa-podcast"></i>
                                }
                                <span>  </span>
                             <a href={!!feed.author?feed.author_contact:"#"} onClick={this.openInNewTab} className="card-link" >
                                {feed.author}
                            </a>
                             </div>
                            
                            <div className="card-body">
                            <h4 className="card-title">
                                <a onClick={this.openInNewTab} className="card-link" href={feed.url}>
                                    {feed.title}
                                </a>
                            </h4>
                              <p className="card-text-feed">{feed.description}</p>  
                            </div>
                            
                            <div className="card-footer bg-transparent border-0">
                            <ul className="list-inline">
                                    {feed.tags.map(tag => (
                                        <li key={tag.pk} className="list-inline-item"><span className="badge badge-secondary badge-pill py-1" style={{backgroundColor:tag.tag_color}}>{tag.pk}</span></li>
                                    ))}
                                    {/* <li class="list-inline-item">Nulla volutpat</li> */}
                                </ul>
                                {/* <small className="text-muted">{feed.itemType} | Last updated {new Date(feed.updated_at).toLocaleDateString()}</small> */}
                                <small className="text-muted">
                                {/* { (feed.itemType === "BLOG") &&
                                <i className="fas fa-blog"></i>
                                }
                                { (feed.itemType === "PODCAST") &&
                                <i className="fas fa-podcast"></i>
                                }
                                <span> </span> */}
                                {`Last updated ${new Date(feed.updated_at).toLocaleDateString()}`}</small>
                            </div>
                        </div>
                    </div>
                    
                ))}
            {/* </div>  */}
        </div>
        
      </div>
    )
  }
}

const mapStateToProps = state => ({
    selected:state.feeds.selected,
    feeds: state.feeds.feeds,
    blog_next: state.feeds.blog_next,
    podcast_next:state.feeds.podcast_next,
    refresh_feed:state.feeds.refresh_feed
});

export default connect(mapStateToProps, {getFeeds,getMore,getBlogs,getFilter})(Feed);
